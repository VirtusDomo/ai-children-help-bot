import pygame as pg

pg.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

eyesImg = pg.image.load('eyes.jpg')
faceImg = pg.image.load('default-face.jpg')
talkingImg = pg.image.load('eyes-mouth.jpg')

clock = pg.time.Clock()
gameDisplay = pg.display.set_mode((537,403))

while True:
    gameDisplay.fill(black)
    gameDisplay.blit(faceImg, (0,0))
    pg.display.flip()
    clock.tick(4)
    gameDisplay.blit(talkingImg, (0,0))
    pg.display.flip()
    clock.tick(4)