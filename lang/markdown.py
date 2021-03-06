from talon.voice import Context, Key

context = Context("markdown")

context.keymap(
    {
     "insert task": "OSGD-",
     "insert list": "* ",
     "insert sob list": "  * ",
     "insert break": "</br>",
     "insert code": ["__``__", Key("left"), Key("left"), Key("left")],
     "insert bold": ["____", Key("left"), Key("left")],
     "surround code": "__`",
     "surround bold": "__",
     "surround italic": "_",
     "surround tick": "`",
     "surround link": ["[", Key("right"), Key("right"), "("],
    }
)
