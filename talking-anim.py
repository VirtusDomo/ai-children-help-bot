import pygame as pg
import time
import sys

pg.init
black = (0,0,0)
white = (255,255,255)

faceImg = pg.image.load('resources/default-face.jpg')
talkingImg = pg.image.load('resources/eyes-mouth.jpg')
talkingImg2 = pg.image.load('resources/mouth2.jpg')
talkingImg3 = pg.image.load('resources/mouth3.jpg')

clock = pg.time.Clock()
gameDisplay = pg.display.set_mode((537,403))

def talking(seconds):
    t_end = time.time() + seconds
    speed = 5
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
    #return


close = time.time() + 20

while time.time() < close:
    wait = time.time() + 5
    while time.time() < wait:
        gameDisplay.blit(faceImg, (0,0))
        pg.display.flip()
    talking(10)

pg.display.quit()
pg.quit()
sys.exit()
