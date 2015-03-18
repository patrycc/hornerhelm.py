import pygame
import os

editor = {
"war" : [0,450, "war.png"],
"guard" : [90,450, "guard.png"],
"might" : [180,450, "might.png"],
"trick" : [270,450, "trick.png"],
"heal" : [360,450, "heal.png"],
"accept" : [450,450, "accept.png"]
}

class Buttons(object):
        
        def __init__(self):
                pygame.init()
