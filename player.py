import pygame, sys, math
from level import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = [0,0]
        self.level = None
        self.health = 100
        self.defence = 1.5
        self.ac = 1
    
    def update(self, callback):
        self.rect.move_ip(self.movement)
        if len(pygame.sprite.spritecollide(self, self.level.walls, dokill = False)) >= 1:
            if pygame.sprite.collide_rect(self, self.level.exit):
                callback(1)
            if pygame.sprite.collide_rect(self, self.level.entrance):
                callback(-1)
            else:
                self.movement[0] *= -1
                self.movement[1] *= -1
                self.rect.move_ip(self.movement)
        self.movement = [0,0]
    
    def defend(self, base_damage):
        if self.health <= 0:
            sys.exit()
        damage = base_damage / (self.defence * self.ac)
        self.health -= math.floor(damage)

    def upLevel(self, level):
        self.movement = [0,0]
        self.level = level
        self.rect.topleft = level.startpos
        player = Player("images/player/alchemist.gif", [0,0])
        randomLevel(player)
        screen_info = pygame.display.Info()
        size = (width, height)=(screen_info.current_w, screen_info.current_h)
        screen = pygame.display.set_mode(size)
        level.draw(screen)

    def downLevel(self, level):
        self.movement = [0,0]
        self.level = level
        self.rect.topleft = level.startpos
        player = Player("images/player/alchemist.gif", [0,0])
        randomLevel(player)
        screen_info = pygame.display.Info()
        size = (width, height)=(screen_info.current_w, screen_info.current_h)
        screen = pygame.display.set_mode(size)
        level.draw(screen)

    def changex(self, change):
        self.movement[0] = change
    
    def changey(self, change):
        self.movement[1] = change

    def draw(self, screen):
        screen.blit(self.image, self.rect)