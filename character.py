import pygame as pg

class Character(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
        self.image = pg.Surface([20, 20])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.maxMoves = 3
        self.moves = self.maxMoves
        self.health = 100
        self.damage = 50
        self.attacked = False
        self.type = None
    
    def update(self, events):
        """update character when clicked"""
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print("Clicked")
    
    def onClicked(self):
        """method for character when they are clicked"""
    

