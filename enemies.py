import pygame, random

pygame.init()

screen_info = pygame.display.Info()
size = (width, height)=(screen_info.current_w, screen_info.current_h)

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
        self.reload = 35
    def update(self):
        if pygame.sprite.collide_rect(self, self.level.player):
            self.reload -=1
            if self.reload == 0:
                self.reload = 35
                self.level.player.defend(self.atk)
        self.rect.move_ip(self.movement)
        self.movement = [0,0]
        if self.rect.centery < 0:
            self.rect.centery = height/2
        elif self.rect.centery > height:
            self.rect.centery = height/2
        if self.rect.centerx < 0:
            self.rect.centerx = width/2
        elif self.rect.centerx > width:
            self.rect.centerx = width/2