import pygame as pg
import time
import sys

pg.init
black = (0,0,0)
white = (255,255,255)

<<<<<<< HEAD
eyesImg = pg.image.load('resources/eyes.jpg')
faceImg = pg.image.load('resources/default-face.jpg')
talkingImg = pg.image.load('resources/eyes-mouth.jpg')
=======
faceImg = pg.image.load('default-face.jpg')
talkingImg = pg.image.load('eyes-mouth.jpg')
talkingImg2 = pg.image.load('mouth2.jpg')
talkingImg3 = pg.image.load('mouth3.jpg')
>>>>>>> d6e81b6c1ec194b0793e8cbd8b1d2274f1f0ba73

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
        gameDisplay.blit(talkingImg2, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(faceImg, (0,0))
        pg.display.flip()
<<<<<<< HEAD
        clock.tick(4)
    #return
=======
        clock.tick(speed)
    return
>>>>>>> d6e81b6c1ec194b0793e8cbd8b1d2274f1f0ba73


close = time.time() + 40

while time.time() < close:
    wait = time.time() + 5
    while time.time() < wait:
        gameDisplay.blit(faceImg, (0,0))
        pg.display.flip()
    talking(10)

pg.display.quit()
pg.quit()
<<<<<<< HEAD
quit()
=======
sys.exit()
>>>>>>> d6e81b6c1ec194b0793e8cbd8b1d2274f1f0ba73
