import pygame

BOX_SIZE = 16

def drawBox(window, color, pos):
    r = pygame.Rect((pos[0] + BOX_SIZE/2, pos[1] + BOX_SIZE/2), (BOX_SIZE, BOX_SIZE))
    pygame.draw.rect(window, color, r)
    
