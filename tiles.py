import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Door(Tile):
    def __init__(self, lockedImage, unlockedImage, pos, unlocked):
        if unlocked:
            super().__init__(unlockedImage, pos)
        else:
            super().__init__(lockedImage, pos)
        self.lockedImage = lockedImage
        self.unlockedImage = unlockedImage
        self.unlocked = unlocked

    def unlock(self):
        self.unlocked = True
        self.image = pygame.image.load(self.unlockedImage)