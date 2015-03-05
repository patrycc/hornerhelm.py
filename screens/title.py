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

class Title(object):
        nein = "nein"
        def __init__(self):
                screen = pygame.display.set_caption("Hornerhelm [conceptual]")
                screen = pygame.display.set_mode((640, 480))
                screen.blit(get_image('img/title_bg.png'), (0, 0))

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
