import ctypes
import pygame
from plyer import notification

def popup(title, message, file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)
    pygame.mixer.quit()
    notification.notify(
        title="Reminder Completed",
        message=message,
        app_name="Koala Reminder",
        app_icon=None,  
        timeout=10
    )

#series:
# innit / load
# play sound 
# display notifis
# end
# popup('Reminder', 'Note Value', 'src\\notification.mp3')
