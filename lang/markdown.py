from talon.voice import Context, Key

context = Context("markdown")

context.keymap(
    {
     "insert list": "* ",
     "insert sob list": "  * ",
     "insert break": "</br>",
     "insert code": "__``__",
     "surround code": "__`",
     "surround bold": "__",
     "surround italic": "_",
     "surround tick": "`",
     "surround link": ["[", Key("right"), Key("right"), "("],
    }
)
