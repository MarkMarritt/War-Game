import pygame as pg
from graphics import dWidth, dHieght

pg.init()
screen = pg.display.set_mode((dWidth, dHieght))
clock = pg.time.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    
    pg.display.update()
