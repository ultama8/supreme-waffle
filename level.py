import pygame, random
from tiles import *
from enemies import *

class Level(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.player = player
        self.startpos = (0,0)
        self.endpos = (0,0)
        self.entrance = None
        self.exit = None
     
    def draw(self, screen):
        self.walls.draw(screen)
        self.floors.draw(screen)
        self.enemies.draw(screen)
        self.player.draw(screen)

    def update(self, callback):
        self.enemies.update()
        self.player.update(callback)

class randomLevel(Level):
    def __init__(self, player):
        super().__init__(player)
        self.generate_level()

    def placeEntrance(self, gamemap):
        for i in range(len(gamemap)):
            for j in range(1, len(gamemap[0])):
                if gamemap[i][j] == "f":
                    self.startpos = (j*32, i*32)
                    gamemap[i][j-1] = "s"
                    return

    def placeExit(self, gamemap):
        for i in range(len(gamemap) - 2, 0, -1):
            for j in range(1, len(gamemap[0])):
                if gamemap[i][j] == "f":
                    self.endpos = (i*32, j*32)
                    gamemap[i][j-1] = "e"
                    return

    def draw(self, screen):
        super().draw(screen)
    def generate_level(self):
        screen_info = pygame.display.Info()
        gamemap = []
        for i in range((screen_info.current_w // 48) + 1):
            gamemap.append(["w"] * ((screen_info.current_w // 32) + 1))
        fnum = int((len(gamemap) * len(gamemap[0])) * .5)
        count = 0
        tile = [len(gamemap) // 2, len(gamemap[0]) // 2]
        while count < fnum:
            if gamemap[tile[0]][tile[1]] != 'f':
                gamemap[tile[0]][tile[1]] = 'f'
                count += 1
            move = random.randint(1, 4)
            if move == 1 and tile[0] > 1:
                tile[0] -= 1
            elif move == 2 and tile[0] < (len(gamemap) - 3):
                tile[0] += 1
            elif move == 3 and tile[1] > 1:
                tile[1] -= 1
            elif move == 4 and tile[1] < (len(gamemap[1]) - 3):
                tile[1] += 1
        
        self.placeEntrance(gamemap)
        self.placeExit(gamemap)

        for y in range(len(gamemap)):
            for x in range(len(gamemap[0])):
                if gamemap[y][x] == "w":
                    self.walls.add(Tile((x*32, y*32), "images/tiles/wall31.gif"))
                if gamemap[y][x] == "f":
                    self.floors.add(Tile((x*32, y*32), "images/tiles/floor33.gif"))
                elif gamemap[y][x] == "s":
                    self.entrance = Tile((x*32, y*32), "images/tiles/door13.gif")
                    self.floors.add(self.entrance)
                elif gamemap[y][x] == "e":
                    self.exit = Tile((x*32, y*32), "images/tiles/door21.gif")
                    self.floors.add(self.exit)
        for y in range(3):
            e = Enemies("images/monsters/bat.gif", random.choice(self.floors.sprites()).rect.center, self)
            self.enemies.add(e)
