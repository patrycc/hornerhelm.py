import pygame
import os
from utils import buttons


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def draw_buttons(buttons, screen):
        for b in buttons:
                button = buttons[b]
                screen.blit(get_image('img/icon/'+button[2]), (button[0],button[1]))

def click_button(posi, buttons):
        x = posi[0]
        y = posi[1]

        for b in buttons:
                button = buttons[b]
                if x > button[0] and y > button[1] and x < (button[0]+90) and y < (button[1]+90):
                        print(button[2])

class Editor(object):
        screenpls = 1
        def __init__(self):

                pygame.init()

                editorClock = pygame.time.Clock()
                
                screen = pygame.display.set_caption("Hornerhelm [conceptual]")
                screen = pygame.display.set_mode((540, 540))
                screen.blit(get_image('img/editor_bg.png'), (0, 0))

                editorLoop = True

                buttonspls = buttons.editor
                draw_buttons(buttonspls, screen)

                while editorLoop:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        titleLoop = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1: # left click
                                        #editorLoop = False
                                        click_button(event.pos, buttonspls)
                                        
                        pygame.display.flip()
                        editorClock.tick(60)
