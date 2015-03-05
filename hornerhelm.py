import pygame
import os
from screens import title

pygame.init()

clock = pygame.time.Clock()

running = True

myTitle = title.Title()

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        pygame.display.flip()
        clock.tick(60)
