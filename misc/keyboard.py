from talon.voice import Context, Key, press

from talon import ctrl

ctx = Context("keyboard")

ctx.keymap({
    "hold ctrl": lambda m: (ctrl.key_press("cmd", ctrl=True, down=True)),
    "release ctrl": lambda m: (ctrl.key_press("cmd", ctrl=True, up=True)),

    "hold shift": lambda m: (ctrl.key_press("shift", shift=True, down=True)),
    "release shift": lambda m: (ctrl.key_press("shift", shift=True, up=True)),

    "hold (alt | ault | old)": lambda m: (ctrl.key_press("alt", alt=True, down=True)),
    "release (alt | ault | old)": lambda m: (ctrl.key_press("alt", alt=True, up=True)),

    "hold command": lambda m: (ctrl.key_press("cmd", cmd=True, down=True)),
    "release command": lambda m: (ctrl.key_press("cmd", cmd=True, up=True)),
	
	"release all": lambda m: (ctrl.key_press("cmd", ctrl=True, cmd=True, alt=True, shift=True, up=True)),
})
