'''
Created on 11/06/2009

@author: Vitor
'''
import pygame
from map import *

screen = pygame.display.set_mode((720,624),0,32)
m = Map()
m.ler_arquivo()
m.desenhar_mapa(screen)

while 1:
    pygame.display.flip()
    