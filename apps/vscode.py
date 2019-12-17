from talon.voice import Context, Key, press, Str

context = Context("VSCode", bundle="com.microsoft.VSCode")


context.keymap(
    {
        # Selecting text
        
        # Finding text
        "find": Key("cmd-f"),
        "find in files": Key("cmd-shift-f"),
        
        # Clipboard
        "clone": Key("alt-shift-down"),

        # Navigation
        "go to line": Key("cmd-g"),
        "go back": Key("ctrl--"),
        "go forward": Key("ctrl-shift--"),

        # Navigating Interface
        "explore": Key("shift-cmd-e"),
        "search": Key("shift-cmd-f"),
        "debug": Key("shift-cmd-d"),
        "source control": Key("shift-ctrl-g"),
        "extensions": Key("shift-cmd-x"),
        "open": Key("cmd-p"),
        
        # tabbing
        "next tab": Key("cmd-alt-right"),
        "last tab": Key("cmd-alt-left"),
        "new file": Key("cmd-n"),
        
        # Menu
        "save": Key("cmd-s"),
        "file open": Key("cmd-o"),
        "command": Key("cmd-shift-p"),
        "sidebar": Key("cmd-b"),
        
        # editing
        "bracken": [Key("cmd-shift-ctrl-right")],
        
        # various
        "comment": Key("cmd-/"),
        "complete ": Key("ctrl-space"),
    }
)
