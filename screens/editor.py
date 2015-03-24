import pygame
import os
from utils import buttons

einherjar = [
[]
]

active_e = 0
buttonspls = buttons.editor_menu

clicked_pos = []

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
                if button[3] == 1:
                        screen.blit(get_image('img/icon/'+button[2]), (button[0],button[1]))
                elif button[3] == 2:
                        screen.blit(get_image('img/icon/nein.png'), (button[0],button[1]))

def click_button(pos, buttons):
        global einherjar
        global active_e
        global clicked_pos

        x = pos[0]
        y = pos[1]

        if clicked_pos is not pos:
                clicked_pos = pos

                if len(einherjar[active_e]) == 5 and len(einherjar) < 5:
                        einherjar.append([])
                        active_e = active_e + 1

                for b in buttons:
                        button = buttons[b]
                        if x > button[0] and y > button[1] and x < (button[0]+90) and y < (button[1]+90) and button[3] == 1:
                                if len(einherjar[active_e]) < 5:
                                        einherjar[active_e].append(b)
                print(einherjar)
                print(len(einherjar))

class Editor(object):
        screenpls = 1
        def __init__(self):

                pygame.init()

                editorClock = pygame.time.Clock()
                
                screen = pygame.display.set_caption("Hornerhelm [conceptual]")
                screen = pygame.display.set_mode((540, 540))
                screen.blit(get_image('img/editor_bg.png'), (0, 0))

                editorLoop = True

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
