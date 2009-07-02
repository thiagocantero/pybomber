'''
Created on 14/06/2009

@author: Vitor
'''
import pygame
import os
class Map(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.size = (800, 600)
        self.pos = (0, 0)
        self.bloco_destrutivel = pygame.image.load(os.path.join("images","wall.png"))
        self.bloco_indestrutivel = pygame.image.load(os.path.join("images","pedra_fixa.png"))
        self.background  = pygame.image.load(os.path.join("images","meuCenario.PNG"))
        self.matriz = []
        self.matriz_arquivo = []
        self.tamanho_mapa = [13,11]
        #inicia a matriz
        for i in range(self.tamanho_mapa[0]):
            l1 = []
            for j in range(self.tamanho_mapa[1]):
                l1.append(0)
            self.matriz.append(l1)
        
    
    def ler_arquivo(self):
        arquivo_mapa = open("maps/mapa.txt")
        for linha in arquivo_mapa.readlines():
            self.matriz_arquivo.append(linha.strip("\r\n").split(" "))
        
        
        
    def desenhar_mapa(self,screen):
        tamanho_do_bloco = 48
        coluna = 48
        screen.blit(self.background, (0,0))
        for i in range(self.tamanho_mapa[1]):
            for j in range(self.tamanho_mapa[0]):
                if self.matriz_arquivo[i][j] == '1':
                    screen.blit(self.bloco_destrutivel,(j*tamanho_do_bloco + coluna,i*tamanho_do_bloco+coluna))
                if self.matriz_arquivo[i][j] == '2':
                    screen.blit(self.bloco_indestrutivel,(j*tamanho_do_bloco + coluna,i*tamanho_do_bloco+coluna))
        
        