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
m.jogadores = []
bomber = Bomberman()
m.jogadores.append(bomber)

def atualiza(self):
    for jogador in m.jogadores:
        if jogador.isVivo:
            jogador.atualiza(pygame.time.get_ticks(),teclado.get())
            screen.blit(jogador.image,jogador.pos)
            
            
        
    
    

while 1:
    pygame.display.flip()
    