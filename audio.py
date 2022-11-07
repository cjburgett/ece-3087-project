import pygame

def run(message):
    
    path = "robot2.mp3"
    path2 = "HB.mp3"
    
    pygame.mixer.init()

    speaker_volume = 100

    pygame.mixer.music.set_volume(speaker_volume)
    if (message == "no no I do not like the cat"):
        pygame.mixer.music.load(path)
    else:
        pygame.mixer.music.load(path2)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy() == True):
#         print(123)
        continue
    
if __name__ == "__main__":
    run("no no I do not like the ca")
