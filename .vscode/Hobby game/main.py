import pygame
import sys
import time
import random
import threading
from client import *
from player import *

from pygame.locals import *

# Pygame things
FPS = 60
pygame.init()
fpsClock=pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

if __name__ == '__main__':
    color = (0, 0, 0)
    player = Player([320, 300])
    client = Client("127.0.0.1", 8080)
    client.connect()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                client.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    #print("JUMP")
                    player.jump()
                if event.key == K_d:
                    player.move([1, 0])
                if event.key == K_a:
                    player.move([-1, 0])
                if event.key == K_ESCAPE:
                    client.quit()
                    pygame.quit()
                    sys.exit()


        surface.fill((255,255,255))
        player.update()
        player.draw(surface)

        for p in client.getPlayers():
            p[1].update()
            p[1].draw(surface)

        screen.blit(surface, (0,0))

        pygame.display.flip()
        pygame.display.update()
        player.update()
        client.update(player.getPosition())

        fpsClock.tick(FPS)