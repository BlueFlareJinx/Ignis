import os
from pynput import keyboard

# Keyboared instruction #
print("Press <Alt>+<Shift>+z: Decrease Brightness")
print("Press <Alt>+<Shift>+a: Increase Brightness")

# Updateding cuurent windows brightness #
def getCurrentBrightness():
    currentWindowBrightness = os.popen('powershell -Command "Get-Ciminstance -Namespace root/WMI -ClassName WmiMonitorBrightness | Select -ExpandProperty "CurrentBrightness"').read().strip()
    return int(currentWindowBrightness)

def adjustBrightness(currentWindowBrightness):
    if currentWindowBrightness < 0:
        currentWindowBrightness = 0
    elif currentWindowBrightness > 100:
        currentWindowBrightness = 100
    return currentWindowBrightness


# Decrease function that can decresing value #
def increase():
    currentWindowBrightness = getCurrentBrightness()
    currentWindowBrightness = int(currentWindowBrightness) + 1

    currentWindowBrightness = adjustBrightness(currentWindowBrightness)

    # Brightness command that can decreasing brightness #
    adjust_brightness_command = "powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{0})".format(currentWindowBrightness)
    os.system(adjust_brightness_command)


# increase function that can increase value #
def decrease():
    currentWindowBrightness = getCurrentBrightness() # 100
    currentWindowBrightness = int(currentWindowBrightness) - 1 # 99
    currentWindowBrightness = adjustBrightness(currentWindowBrightness) # 99

    # Brightness command that can increasing brightness #
    adjust_brightness_command = "powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{0})".format(currentWindowBrightness)
    os.system(adjust_brightness_command)


# Hotkeys: Handleing keyboared input #
with keyboard.GlobalHotKeys({'<shift>+<alt>+a': increase,'<shift>+<alt>+z': decrease}) as h:h.join()