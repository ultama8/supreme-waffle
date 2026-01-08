import pygame
import sys
from pygame.locals import *
from level import *
from player import *

pygame.init()

font = pygame.font.SysFont("timesnewroman", 32)
screen_info = pygame.display.Info()
size = (width, height)=(screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
color = (108, 59, 170)
clock = pygame.time.Clock()
current_level = None
player = Player("images/player/alchemist.gif", [0,0])
level = []
levelnum = 0

def gamestart():
    global player, level, current_level, levelnum
    player = Player("images/player/alchemist.gif", [0,0])
    level = [randomLevel(player)]
    levelnum = 0
    current_level = level[levelnum]
    player.upLevel(current_level)

def change_level(change):
    global levelnum, current_level
    if change == 1:
        if levelnum == len(level) - 1:
            level.append(randomLevel(player))
        levelnum += 1
        current_level = level[levelnum]
        player.upLevel(current_level)
    elif change == -1:
        if levelnum == len(level) - 1:
            level.append(randomLevel(player))
        if levelnum == 0:
            pass
        if levelnum > 0:
            levelnum -= 1
            current_level = level[levelnum]
            player.downLevel(current_level)

def main():
    global current_level, levelnum
    running = True
    gamestart()
    while running:
        clock.tick(60)
        # Handle quitting the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_r:
                    gamestart()
                if event.key == K_u:
                    level.append(randomLevel(player))
                    levelnum += 1
                    current_level = level[levelnum]
                    player.upLevel(current_level)
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            player.changey(-5)
        if keys[K_s]:
            player.changey(5)
        if keys[K_d]:
            player.changex(5)
        if keys[K_a]:
            player.changex(-5)
        screen.fill(color)
        current_level.draw(screen)
        current_level.update(change_level)
        text = font.render(f"{player.rect.center}", True, (230,230,230))
        text_rect = text.get_rect()
        text_rect.topright = (width, 0)
        screen.blit(text, text_rect)
        text2 = font.render(f"Health: {player.health}", True, (230,230,230))
        text_rect2 = text2.get_rect()
        text_rect2.topright = (width - 5, 50)
        screen.blit(text2, text_rect2)
        pygame.display.flip()

if __name__ == "__main__":
    main()