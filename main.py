import pygame as pg
from graphics import dWidth, dHieght, background_img
from character import Character


character = Character(20, 20)
group = pg.sprite.GroupSingle(character)

pg.init()
screen = pg.display.set_mode((dWidth, dHieght))
clock = pg.time.Clock()
screen.blit(background_img, (0,0))
running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    group.update(events)
    group.draw(screen)
    
    pg.display.update()
