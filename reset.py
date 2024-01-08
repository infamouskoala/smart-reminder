# This file removes the backdoor from startup
import os
import time
startup = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
file = f"{startup}\\timer.bat"
print("Removing the autorun task...")
time.sleep(2)
os.remove(file)
print(f">> {file} has been removed.")
print("Press any key to close this window")
input()