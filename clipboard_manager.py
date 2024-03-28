import keyboard


def windows_v_hotkey():
    print("hotkey")


keyboard.add_hotkey("windows+v", windows_v_hotkey)

keyboard.wait()
