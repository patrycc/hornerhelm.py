import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

class Editor(object):
        screenpls = 1
        def __init__(self):

                pygame.init()

                editorClock = pygame.time.Clock()
                
                screen = pygame.display.set_caption("Hornerhelm [conceptual]")
                screen = pygame.display.set_mode((640, 640))
                screen.blit(get_image('img/editor_bg.png'), (0, 0))

                editorLoop = True

                while editorLoop:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        titleLoop = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1: # left click
                                        editorLoop = False
                                      
                        print("editor")
                        pygame.display.flip()
                        editorClock.tick(60)
