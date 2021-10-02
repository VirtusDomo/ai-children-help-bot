import pygame as pg
import time

pg.init()

black = (0,0,0)
white = (255,255,255)

eyesImg = pg.image.load('eyes.jpg')
faceImg = pg.image.load('default-face.jpg')
talkingImg = pg.image.load('eyes-mouth.jpg')

clock = pg.time.Clock()
gameDisplay = pg.display.set_mode((537,403))

def talking(seconds):
    t_end = time.time() + seconds
    while time.time() < t_end:
        gameDisplay.blit(talkingImg, (0,0))
        pg.display.flip()
        clock.tick(4)
        gameDisplay.blit(faceImg, (0,0))
        pg.display.flip()
        clock.tick(4)
    return


close = time.time() + 60

while time.time() < close:
    gameDisplay.fill(black)
    gameDisplay.blit(faceImg, (0,0))
    pg.display.flip()
    talking(10)
    clock.tick(1)

pg.quit()
quit()