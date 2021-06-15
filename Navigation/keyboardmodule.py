import keyboard


def pg1(a):
    print("You are at Page1")
def pg2(a):
    print("You are at Page2")

keyboard.press_and_release('shift+s, space')
keyboard.add_hotkey('ctrl+left', lambda: pg1('a'))
keyboard.add_hotkey('ctrl+right', lambda: pg2('a'))
keyboard.wait()