import pygame, random

class Enemies(pygame.sprite.Sprite):
    def __init__(self, path, pos, level):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = pygame.math.Vector2(0, 0)
        self.movement.rotate_ip(random.randint(0, 359))
        self.level = level
        self.min_distance = 50
        self.health = 30
        self.atk = 5
        self.defence = 2
    def update(self):
        if pygame.sprite.collide_rect(self, self.level.player):
            self.level.player.defend(self.atk)