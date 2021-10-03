import pygame as pg
from pygrame import mixer
import time

pg.init()

black = (0,0,0)
white = (255,255,255)

faceImg = pg.image.load('default-face.jpg')
talkingImg = pg.image.load('eyes-mouth.jpg')
talkingImg2 = pg.image.load('mouth2.jpg')
talkingImg3 = pg.image.load('mouth3.jpg')

clock = pg.time.Clock()

def talking(seconds):
    t_end = time.time() + seconds
    speed = 5
    gameDisplay = pg.display.set_mode((537,403))
    while time.time() < t_end:
        gameDisplay.blit(talkingImg, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(talkingImg2, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(talkingImg3, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(faceImg, (0,0))
        pg.display.flip()
        clock.tick(speed)
    return


mixer.music.load('Ariana Grande - pov (audio).mp3')
mixer.music.play()

close = time.time() + 20
while time.time() < close:
    gameDisplay = pg.display.set_mode((537,403))
    gameDisplay.blit(faceImg, (0,0))
    pg.display.flip()
    talking(10)

pg.quit()
quit()