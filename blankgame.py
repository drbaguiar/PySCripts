# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 13:49:38 2015

@author: bryan_000
"""
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Pygame World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()