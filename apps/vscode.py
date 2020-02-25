from talon.voice import Context, Key, press, Str

context = Context("VSCode", bundle="com.microsoft.VSCode")


context.keymap(
    {
        # Selecting text
        
        # Finding text
        "(find | search)": Key("cmd-f"),
        "find in files": Key("cmd-shift-f"),
        
        # Clipboard
        "clone": Key("alt-shift-down"),

        # Navigation
        "go to line": Key("cmd-g"),
        "go back": Key("ctrl--"),
        "go forward": Key("ctrl-shift--"),

        # Navigating Interface
        "explore": Key("shift-cmd-e"),
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

		# cursors
		"cursor above": Key("alt-shift-cmd-up"),
		"cursor below": Key("alt-shift-cmd-down"),

        # 
        "(peak | peek) definition": Key("alt-f12"),
        "go to definition": Key("f12"),
        "references": Key("shift-f12"),
        "zen mode": [Key("cmd-k"), Key("z")],
        "change name": Key("f2"),
    }
)
