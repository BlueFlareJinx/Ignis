import os

# # Create Ignis folder in AppData
# os.system('mkdir "%localappdata%\\Ignis"')

# # Copy Ignis files into AppData\Ignis folder
# os.system('copy "Ignis.py" "%localappdata%\\Ignis\\ignis.py"')
# os.system('copy "gui.py" "%localappdata%\\Ignis\\gui.py"')
# os.system('copy "run.bat" "%localappdata%\\Ignis\\run.bat"')

os.system('copy "ignis.exe" "%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ignis.exe"')

os.popen('"%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ignis.exe"')
