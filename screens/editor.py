import pygame
import os
from utils import buttons

einherjar = [
[]
]

buttonspls = buttons.editor_menu
gbs = buttons.gbs
party_validity = False
active_e = 0

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

def redraw(screen):
        screen.fill((0, 0, 0))
        screen.blit(get_image('img/editor_bg.png'), (0, 0))

        einzahler = 0

        for ein in einherjar:
                for r in range(0,5):
                        screen.blit(get_image('img/icon/select/empty.png'), (r*gbs,(einzahler*gbs)) )
                for e in range(0,len(ein)):
                        temp_e = einherjar[einzahler][e]
                        screen.blit(get_image('img/icon/select/'+temp_e+'.png'), (e*gbs,(einzahler*gbs)) )
                screen.blit(get_image('img/icon/nein.png'), (5*gbs,(einzahler*gbs)) )
                einzahler = einzahler +1
                                

        for b in buttonspls:
                button = buttonspls[b]
                if button[3] == 1:
                        screen.blit(get_image('img/icon/'+button[2]), (button[0],button[1]))
                elif button[3] == 2:
                        screen.blit(get_image('img/icon/nein.png'), (button[0],button[1]))
        

def check_validity():
        global party_validity
        global buttonspls
        buttonspls["accept"][3] = 2
        valid = True
        for ein in einherjar:
                if len(ein) is not 5:
                        print("is not valid!")
                        valid = False
        print(valid)
        
        if (valid is True):
                party_validity = True
                buttonspls["accept"][3] = 1


def click_button(pos, buttons, screen):
        global einherjar
        global clicked_pos
        global active_e

        x = pos[0]
        y = pos[1]

        if clicked_pos is not pos:
                clicked_pos = pos

                for b in buttons:
                        button = buttons[b]
                        if x > button[0] and y > button[1] and x < (button[0]+90) and y < (button[1]+90) and button[3] == 1:

                                if len(einherjar[active_e]) == 5 and len(einherjar) < 5 and b is not "accept":
                                        einherjar.append([])
                                        active_e = active_e + 1

                                if len(einherjar[active_e]) < 5 and b is not "accept":
                                        einherjar[active_e].append(b)
                                
                                if b == "accept":
                                        print("OK")
                print(einherjar)

                check_validity()
                redraw(screen)

class Editor(object):
        screenpls = 1
        def __init__(self):

                pygame.init()

                editorClock = pygame.time.Clock()
                
                screen = pygame.display.set_caption("Hornerhelm [conceptual]")
                screen = pygame.display.set_mode((540, 540))

                editorLoop = True

                redraw(screen)

                while editorLoop:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        titleLoop = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1: # left click
                                        #editorLoop = False
                                        click_button(event.pos, buttonspls, screen)
                                        
                        pygame.display.flip()
                        editorClock.tick(60)
