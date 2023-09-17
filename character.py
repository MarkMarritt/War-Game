import pygame as pg

def clicked():
    print("clicked")

class Character(pg.sprite.Sprite):
    def __init__(self, x, y, action = clicked):
        super().__init__()
        self.type = None
        self.position = (x, y)
        self.maxMoves = 3
        self.moves = self.maxMoves
        self.health = 100
        self.damage = 50
        self.attacked = False
        self.image = pg.Surface([20, 20])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.action = action
    
    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.action()

