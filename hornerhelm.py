import pygame
import os
from screens import title
from screens import editor

pygame.init()

clock = pygame.time.Clock()

running = True

showScreen = 1

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        print(showScreen)
        if (showScreen == 1):
                myTitle = title.Title()
                showScreen = myTitle.screenpls
        elif (showScreen == 2):
                myEditor = editor.Editor()
                showScreen = myEditor.screenpls

        pygame.display.flip()
        clock.tick(60)
