import pygame
import os

editor = {
"war" : [0,0, "war.png"],
"guard" : [100,0, "guard.png"],
"might" : [200,0, "might.png"],
"trick" : [300,0, "trick.png"],
"heal" : [400,0, "heal.png"]
}

class Buttons(object):
        
        def __init__(self):
                pygame.init()
