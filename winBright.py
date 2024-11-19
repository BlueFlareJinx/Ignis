import os
from pynput import keyboard

# Keyboared instruction #
print("Press <Alt>+<Shift>+z: Decrease Brightness")
print("Press <Alt>+<Shift>+a: Increase Brightness")

# Updateding cuurent windows brightness #
def getCurrentBrightness():
    command = "powercfg /q SCHEME_CURRENT SUB_VIDEO VIDEONORMALLEVEL"
    currentWindowBrightness = os.popen(command).read().strip()

    index = currentWindowBrightness.find("Current AC Power Setting Index:") + len("Current AC Power Setting Index: ")
    hexVal = currentWindowBrightness[index : index + 10]

    currentWindowBrightness = int(hexVal, 16)

    # Printing brigtnesss 
    # print(currentWindowBrightness)
    
    return currentWindowBrightness

def adjustBrightness(currentWindowBrightness):
    if currentWindowBrightness < 0:
        currentWindowBrightness = 0
    elif currentWindowBrightness > 100:
        currentWindowBrightness = 100
    return currentWindowBrightness


# Decrease function that can decresing value #
def increase():
    currentWindowBrightness = getCurrentBrightness()
    currentWindowBrightness = currentWindowBrightness + 1

    currentWindowBrightness = adjustBrightness(currentWindowBrightness)

    # Brightness command that can decreasing brightness #
    adjust_brightness_command = "powercfg -setdcvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    adjust_brightness_command = "powercfg -setacvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    os.system(adjust_brightness_command)


# increase function that can increase value #
def decrease():
    currentWindowBrightness = getCurrentBrightness() # 100
    currentWindowBrightness = currentWindowBrightness - 1 # 99
    currentWindowBrightness = adjustBrightness(currentWindowBrightness) # 99

    # Brightness command that can increasing brightness #
    adjust_brightness_command = "powercfg -setdcvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    adjust_brightness_command = "powercfg -setacvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    os.system(adjust_brightness_command)


# Hotkeys: Handleing keyboared input #
with keyboard.GlobalHotKeys({'<shift>+<alt>+a': increase,'<shift>+<alt>+z': decrease}) as h:
    h.join()
