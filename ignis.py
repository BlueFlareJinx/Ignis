import os
from pynput import keyboard
import tkinter as tk
from tkinter import ttk
import gui

# Keyboared instruction #
# print("Press <Alt>+<Shift>+z: Decrease Brightness")
# print("Press <Alt>+<Shift>+a: Increase Brightness")

# Updateding cuurent windows brightness #
def getCurrentBrightness():
    command = "powercfg /q SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb"
    currentWindowBrightness = os.popen(command).read().strip()

    index = currentWindowBrightness.find("Current AC Power Setting Index:") + len("Current AC Power Setting Index: ")
    hexVal = currentWindowBrightness[index : index + 10]

    currentWindowBrightness = int(hexVal, 16)

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

    # GUI toast popup
    root.after(0, lambda: gui.show_toast("Brightness: {0}".format(currentWindowBrightness), 3000))

    # Brightness command that can decreasing brightness #
    adjust_brightness_command = "powercfg -setdcvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    os.popen(adjust_brightness_command)

    adjust_brightness_command = "powercfg -setacvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    os.popen(adjust_brightness_command)

# increase function that can increase value #
def decrease():    
    currentWindowBrightness = getCurrentBrightness()
    currentWindowBrightness = currentWindowBrightness - 1 
    currentWindowBrightness = adjustBrightness(currentWindowBrightness) 

    # GUI toast popup
    root.after(0, lambda: gui.show_toast("Brightness: {0}".format(currentWindowBrightness), 3000))

    # Brightness command that can increasing brightness #
    adjust_brightness_command = "powercfg -setdcvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    os.popen(adjust_brightness_command)

    adjust_brightness_command = "powercfg -setacvalueindex SCHEME_CURRENT SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {0} && powercfg /setactive SCHEME_CURRENT".format(currentWindowBrightness)
    os.popen(adjust_brightness_command)

# Hotkeys: Handleing keyboared input #
GlobalHotKeys = keyboard.GlobalHotKeys({'<shift>+<alt>+a': increase,'<shift>+<alt>+z': decrease})
GlobalHotKeys.start()

# # Main Application
# root = tk.Tk()
# root.withdraw()  # Hide the root window

# # Define custom styles
# style = ttk.Style()
# style.configure("Toast.TFrame", background="#333", relief="flat")
# style.configure("Toast.TLabel", background="#333", foreground="#fff", font=("Arial", 14))

# root.mainloop()

 #Example usage
root = tk.Tk()
root.withdraw()  # Hide the main window
# show_toast("This is a toast message!", duration=3000)
root.mainloop()

# # Hotkeys: Handleing keyboared input #
# with keyboard.GlobalHotKeys({'<shift>+<alt>+a': increase,'<shift>+<alt>+z': decrease}) as h:
#     h.join()
