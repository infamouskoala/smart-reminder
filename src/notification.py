import ctypes
import pygame

def notification(title, message, file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)
    pygame.mixer.quit()

#series:
# innit / load
# play sound 
# display notifis
# end
# notification('Reminder', 'Note Value', 'notification.mp3')