class character:
    def __init__(self, position):
        self.type = None
        self.position = position
        self.maxMoves = 3
        self.moves = self.maxMoves
        self.health = 100
        self.damage = 50
        self.attacked = False
