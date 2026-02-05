import pygame, random, math

pygame.init()

screen_info = pygame.display.Info()
size = (width, height)=(screen_info.current_w, screen_info.current_h)

class Enemies(pygame.sprite.Sprite):
    def __init__(self, path, pos, level):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = pygame.math.Vector2(0, 5)
        self.movement.rotate_ip(random.randint(0, 359))
        self.level = level
        self.counter = 30
        self.counter2 = 30
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
        if pygame.Vector2.distance_to(pygame.Vector2(self.rect.center), pygame.Vector2(self.level.player.rect.center)) < 300:
            selfVect = pygame.math.Vector2(self.rect.center[0], self.rect.center[1])
            playerPosVect = pygame.math.Vector2(self.level.player.rect.center[0], self.level.player.rect.center[1])

            diff = (selfVect - playerPosVect) * -1

            if diff[0] > 0:
                diff[0] = 1.5
            elif diff[0] < 0:
                diff[0] = -1.5
            if diff[1] > 0:
                diff[1] = 1.5
            elif diff[1] < 0:
                diff[1] = -1.5
            
            self.movement = diff
        else:
            temp_move = self.movement
            if self.counter2 <= 0:
                rand = random.randint(-2, 2)
                rand2 = random.randint(-2, 2)
                temp_move[0] = rand
                temp_move[1] = rand2
                self.counter2 = random.randint(10, 30)
            else:
                self.counter2 -= 1
            
            self.movement = temp_move
            if self.counter <= 0:
                self.movement.rotate_ip(random.randint(0, 360))
                self.counter = random.randint(10, 50)
            else:
                self.counter -= 1
        self.rect.move_ip(self.movement)
        self.movement = pygame.math.Vector2(0, 0)
        if self.rect.centery < 0:
            self.rect.centery = height/2
        elif self.rect.centery > height:
            self.rect.centery = height/2
        if self.rect.centerx < 0:
            self.rect.centerx = width/2
        elif self.rect.centerx > width:
            self.rect.centerx = width/2
    
    def defend(self, base_damage, hit_type, fire_duration):
        if hit_type == "Normal":
            damage = base_damage / self.defence
            self.health -= math.floor(damage)
        if hit_type == "Fire":
            fire_counter = fire_duration * 2
            if fire_counter > 0:
                damage = (base_damage / self.defence) + 5
                self.health -= math.floor(damage)
                fire_counter -= 1
            else:
                damage = base_damage / self.defence
                self.health -= math.floor(damage)